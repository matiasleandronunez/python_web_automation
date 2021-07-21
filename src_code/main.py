from helpers import before_run_hooks

if __name__ == '__main__':
    # SETUP HOOKS
    before_run_hooks.setup_before_run()

    from behave import __main__ as behave_executable
    behave_executable.main(None)