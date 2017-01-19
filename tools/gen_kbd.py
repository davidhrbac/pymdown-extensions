import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join('.')))

import pymdownx.kbd as kbd

STYLE = '''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,400i,700|Roboto+Mono" class="--apng-checked">
<style>
html {
  font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
  line-height: 1.6;
  font-size: 1.2rem;
}
.kbd.input {
  font-family: "Roboto Mono","Courier New",Courier,monospace;
  padding: 0 .29412em;
  border-radius: .3rem;
  font-weight: 400;
  background-color: #2196f3;
  color: #fff;
  font-size: 85%;
  box-shadow: 0 2px 2px 0 rgba(0,0,0,.1), 0 1px 5px 0 rgba(0,0,0,.1), 0 3px 1px -2px rgba(0,0,0,.1);
}
.kbd.input:before {
  color: rgba(255, 255, 255, .7);
  font-size: 85%;
  bottom: 2;
  position: relative;
  bottom: 0.1rem;
}
.kbd.sep {
    color: #888;
    padding: 0 .2rem;
}
.key-command:before {
  content: '\\2318';
  padding-right: 0.2rem;
}

.kbd.key-windows:before {
  content: '\\229E';
  padding-right: 0.2rem;
}

.kbd.key-tab:before {
  content: '\\21B9';
  padding-right: 0.2rem;
}

.kbd.key-caps-lock:before {
  content: '\\21EA';
  padding-right: 0.2rem;
}
</style>
'''

combo = [
  '++win+shift+s++',
  '++cmd+ctrl+d++',
  '++ctrl+alt+"Special"++'
]


def main():
    with open('tests/extensions/kbd.txt', 'w') as f:
        f.write(STYLE)
        f.write('# Keys\n')
        for key in sorted(kbd.keymap.keymap.keys()):
            f.write('++%s++\n' % key)
        f.write('# Aliases\n')
        for key in sorted(kbd.keymap.aliases.keys()):
            f.write('++%s++\n' % key)
        f.write('# Combos\n')
        for key in combo:
          f.write(key + '\n')


if __name__ == "__main__":
    main()
