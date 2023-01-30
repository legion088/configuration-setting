import getpass
import os


def write_in_file_config(username: str) -> None:
    versions = ['1cv8', '1cv8_x32', '1cv8_x86', '1cv8_x64']
    with open(rf'C:\Users\{username}\AppData\Roaming\1C\1CEStart\1CEStart.cfg', 'w') as file:        
        for ver in versions:
            Installedlocations = rf'InstalledLocation=C:\Users\{username}\AppData\local\Programs\{ver}' + '\n'
            file.write(Installedlocations)


def check_exists_path(username: str) -> dict:
    path_error = dict()
    path = [rf'C:\Users\{username}\AppData\Local\Program\1C',
            rf'C:\Users\{username}\AppData\Roaming\1C\1CEStart']
    for pt in path:
        if not os.path.exists(pt):
            path_error['msg'] = f'Не удается найти указанный путь: {pt}, или временный профиль!'
            return path_error
    return path_error


def main():
    username = getpass.getuser()
    errors = check_exists_path(username)
    if not errors:
        write_in_file_config(username)
        print('done')
    else:
        print(errors.get('msg'))


if __name__ == '__main__':
    main()
    os.system("pause")
