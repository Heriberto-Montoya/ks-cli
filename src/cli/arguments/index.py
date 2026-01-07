import argparse


class DefinedArguments:
  def __init__(self):
    self.parser = argparse.ArgumentParser(description="A keystore CLI tool")
    self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")
    self._add_create_parser()
    self._add_list_parser()
    self._pass_vault_parser()

  def _add_create_parser(self):
    create = self.subparsers.add_parser("create", help="Create a new keystore")
    create.add_argument("name", help="Name of the keystore to create")
    create.add_argument("--user", "-u", help="User for the keystore")
    create.add_argument("--password", "-p", help="Password for the keystore")
    create.add_argument("--type", "-t", choices=["credential", "text"], default="text", help="Type of keystore")
    create.add_argument("--value", "-v", help="Value for the keystore (if type is text)")
    

  def _add_list_parser(self):
    ls = self.subparsers.add_parser("list", help="List existing keystores")
    ls.add_argument("--verbose", "-v", action="store_true", help="Show detailed information")
    ls.add_argument("--password", "-p", action="store_true", help="Show password in item credentials keystore")

  def _pass_vault_parser(self):
    pass_vault = self.subparsers.add_parser("passvault", help="Manage password Keystore")
    pass_vault.add_argument("pass", help="Password vault command")

  def parse_arguments(self):
    return self.parser.parse_args()
  
  def help(self):
    self.parser.print_help()
  
