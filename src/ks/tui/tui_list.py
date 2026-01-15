from rich import print as rprint
from rich.console import Console
from rich.table import Table

def print_keystore_list(data: dict, verbose: bool = False, password: bool = False):
  items = []
  
  # Collect items
  for item_name, item_data in data.items():
    key = {
      'name': item_name,
      'type': item_data.get('type_key', None),
      'content': item_data.get('content', None), 
      'user': item_data.get('user', None),
      'password': item_data.get('password', None)
    }
    items.append(key)
  
  if not items:
    print('No items found in keystore.')
    return
  
  console = Console()

  # Create a Table instance and set box=None to remove borders
  table = Table(box=None, title="Keystore Items", show_header=True, header_style="bold magenta ")

  # Define columns
  table.add_column("NAME", style="", no_wrap=True)
  table.add_column("TYPE", style="")
  if verbose:
    table.add_column("USER", style="")
    table.add_column("PASS", style="")
    table.add_column("CONTENT", style="")
  
  # Add rows to the table
  for item in items:  
    if verbose:
      content = item['content']
      # if content and len(str(content)) > 35:
      #   content = str(content)[:32] + '...'
      # else:
      #   content = content or '-'
      
      str_pass = '******' if not password and item['type'] == 'credential' else (item['password'] or '-')
      user = item['user'] or '-'
      table.add_row(
        item['name'],
        item['type'] or '-',
        user,
        str_pass,
        str(content)
      )
    else:
      table.add_row(
        item['name'],
        item['type'] or '-'
      )

  console.print(table)
  print()
