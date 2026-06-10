import sys
from ks.commands.exec_command import ExecCommand
from ks.arguments.index import DefinedArguments
import os


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    █   █  ████       ███  █     ███ 
    █  █  █          █     █      █  
    ███    ███  ████ █     █      █  
    █  █      █      █     █      █  
    █   █ ████        ███  █████ ███ 
    """)
    commands = DefinedArguments()
    args = commands.parse_arguments()

    try:
        if args.command:
            executor = ExecCommand(args)
            executor.execute()
        else:
            commands.help()
    # except Exception:
    #     print(sys.exc_info()[1])
    except KeyboardInterrupt:
        sys.exit(0)
    return

if __name__ == "__main__":
    main()