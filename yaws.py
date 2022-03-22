import itertools, json, yaml

def get_yaml_file(file):
  f = open(file, 'r')
  data = yaml.load(f.read(), Loader=yaml.FullLoader)
  f.close()
  return data

def get_json_file(file):
  f = open(file)
  data = json.loads(f.read())
  f.close()
  return data

def remove_from_list(source_list, to_remove):
  result = list(set(source_list) - set(to_remove))
  result.sort()
  return result

def filter_letters(space, config):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letters = remove_from_list(alphabet, str(config['exclude']).upper())
  if "exclude" in space:
    letters = remove_from_list(letters, str(space['exclude']).upper())
  return letters

def parse_space(space, config):
  if isinstance(space, str):
    return [space.upper()]
  return filter_letters(space, config)

def parse_spaces(config):
  for space in config['spaces']:
    yield parse_space(space, config)

def main():
  config = get_yaml_file('config.yaml')
  valid_words = get_json_file('five-letter-words.json')
  product = itertools.product(*list(parse_spaces(config)))

  for word in product:
    word_string = "".join(word)
    is_valid = all(x.upper() in word_string for x in config['include'])
    if is_valid:
      if word_string.lower() in valid_words:
        print(word_string)

main()