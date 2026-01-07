from rich import print as rprint
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
  
  # Define column widths (Docker style)
  col_name = 30
  col_type = 15
  col_user = 15
  col_pass = 15
  col_content = 25
  
  # Header
  if verbose:
    header =  f"{'NAME':<{col_name}}  {'TYPE':<{col_type}}  {'USER':<{col_user}} {'PASS':<{col_user}}  {'CONTENT':<{col_content}}" 
  else:
    header = f"{'NAME':<{col_name}}  {'TYPE':<{col_type}}" 
  
  rprint("[blue]Keystore Items:[/blue]")
  print(header)

  # Rows
  for item in items:
    if verbose:
      content = item['content']
      if content and len(str(content)) > col_content - 2:
        content = str(content)[:col_content-5] + '...'
      else:
        content = content or '-'
        
      str_pass = '******' if not password and item['type'] == 'credential' else (item['password'] or '-')
      
      user = item['user'] or '-'
      row = f"{item['name']:<{col_name}}  {(item['type'] or '-'):<{col_type}}  {user:<{col_user}} {str_pass:<{col_pass}}  {str(content):<{col_content}}"
    else:
      row = f"{item['name']:<{col_name}}  {(item['type'] or '-'):<{col_type}}"
    
    print(row)
  
  print()
