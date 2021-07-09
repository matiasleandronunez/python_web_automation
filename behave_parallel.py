#Behave parallel custom runner by https://stepupautomation.wordpress.com/2019/03/28/execute-tests-in-parallel-with-behave-bdd/

from multiprocessing import Pool
from subprocess import call, Popen, PIPE
from functools import partial
from glob import glob
import logging
import argparse
import json
from helpers import before_run_hooks

logging.basicConfig(level=logging.INFO, format="[%(levelname)-8s %(asctime)s] %(message)s")
logger = logging.getLogger(__name__)


def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser('Running in parallel mode. Do not use features and tags argument at the same time')
    parser.add_argument('--suite', '-s', help='Please specify the suite you want to run. Default suite is regression',
                        default='regression_suite')
    parser.add_argument('--feature_list', '-l',
                        help='Please specify file path of features or features location you want to run.')
    parser.add_argument('--feature', '-f', help='Please specify feature you want to run.')
    parser.add_argument('--processes', '-p', type=int, help='Maximum number of processes. Default = 5', default=5)
    parser.add_argument('--tags', '-t', help='Please specify behave tags to run')
    parser.add_argument('--outfile_prefix', '-o', help='Please specify outfile prefix to run')
    return parser.parse_args()


def _run_parallel_feature(feature):
    """
    Runs features without tags @sequential
    :param feature: Feature will be run
    :type feature: str
    """
    logger.debug('Processing feature: {}'.format(feature))
    feature_test_log = feature.replace('/', '-')
    cmd = 'behave {feature} --tags ~@sequential>> ./log/{feature_test_log}.txt'.format(feature=feature,
                                                                                       feature_test_log=feature_test_log)
    r = call(cmd, shell=True)
    status = 'Passed' if r == 0 else 'Failed'
    print('{0:50}: {1}!!'.format(feature, status))


def _run_sequential_feature(feature, outfile_prefix):
    """
    Runs features with tags @sequential
    :param feature: Feature will be run
    :type feature: str
    """
    logger.debug('Processing feature: {}'.format(feature))
    feature_test_log = feature.replace('/', '-')
    cmd = 'behave {feature} --tags @sequential --tags {outfile_prefix} >> ~/log/{outfile_prefix}_{feature_test_log}.txt'.format(
        feature=feature, outfile_prefix=outfile_prefix, feature_test_log=feature_test_log)
    r = call(cmd, shell=True)
    status = 'Passed' if r == 0 else 'Failed'
    print('{0:50}: {1}!!'.format(feature, status))


def main():
    """
    Runner
    """
    args = parse_arguments()
    pool = Pool(args.processes)

    #SETUP HOOKS
    before_run_hooks.setup_before_run()

    if not args.feature_list and not args.feature and not args.tags:
        """
        Run all features in system
        """
        features = glob('{suite}/*.feature'.format(suite=args.suite))
    elif args.feature_list and not args.tags:
        """
        Run feature list defined by users
        """
        file = open(args.feature_list)
        features = []
        for feature in file:
            feature = feature.replace('\n', '')
            features.append(feature) if '/' in feature else features.append(args.suite + '/' + feature)
    elif args.feature_list and args.tags:
        """
        Run feature list with specific tag defined by users
        """
        file = open(args.feature_list)
        features = []
        for feature in file:
            feature = feature.replace('\n', '')
            feature = args.suite + '/' + feature if '/' not in feature else feature
            cmd = 'behave {feature} --tags {tag} -d -k -f json --no-summary'.format(feature=feature, tag=args.tags)
            p = Popen(cmd, stdout=PIPE, shell=True)
            out, err = p.communicate()
            if json.loads(out.decode()):
                scenarios = json.loads(out.decode())[0]['elements']
                for scenario in scenarios:
                    features.append(scenario['location'])
    else:
        cmd = ''
        if args.feature and args.tags:
            """
            Run a feature with specific tag
            """
            cmd = 'behave {suite}/{feature} -d -f json --no-summary -t {tags}'.format(
                suite=args.suite, feature=args.feature, tags=args.tags)

        elif args.tags:
            """
            Run tags defined by user input
            """
            cmd = 'behave {suite}/. -d -f json --no-summary -t {tags}'.format(suite=args.suite, tags=args.tags)
        p = Popen(cmd, stdout=PIPE, shell=True)
        out, err = p.communicate()
        scenarios = json.loads(out.decode())[0]['elements']
        features = [scenario['location'] for scenario in scenarios]

    if args.outfile_prefix:
        pool.map(partial(_run_sequential_feature, outfile_prefix=args.outfile_prefix), features)
    else:
        pool.map(_run_parallel_feature, features)


if __name__ == '__main__':
    main()