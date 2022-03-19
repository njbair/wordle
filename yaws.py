import itertools, json

def get_file(file):
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
  letters = remove_from_list(alphabet, config['exclude_letters'])
  if "exclude" in space:
    letters = remove_from_list(letters, space['exclude'])
  return letters

def parse_space(space, config):
  if isinstance(space, str):
    return [space]
  return filter_letters(space, config)

def parse_spaces(config):
  for space in config['spaces']:
    yield parse_space(space, config)

def main():
  config = get_file('config.json')
  valid_words = get_file('five-letter-words.json')
  product = itertools.product(*list(parse_spaces(config)))

  for word in product:
    word_string = "".join(word)
    is_valid = all(x in word_string for x in config['include_letters'])
    if is_valid:
      if word_string.lower() in valid_words:
        print(word_string)

main()