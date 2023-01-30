![1c](https://github.com/legion088/configuration-setting/blob/master/img/1c.jpg)
### Описание:
Скрипт применяется для автоматизации настройки конфигурационного файла 1CEStart.cfg для программы 1С: Предприятие.
### Для чего это необходимо?
В случаях если клиент 1С установлен в профиле пользователя: %userprofile%\AppData\Local\Program\1C, то программа 1cestart.exe будет работать неккоректно, так как параметр InstalledLocation для запуска клиента ищет каталоги C:\Program Files\ и C:\Program Files(x86)\ соответственно.<br /><br />
Рабочий пример: `InstalledLocation=C:\Program Files\1cv83` <br />
Параметр `InstalledLocation=%userprofile%\AppData\Local\Program\1C` - работать не будет, обязательно нужно определить %userprofile%.
<br /><br />
Решение данной проблемы - подключиться к пользователю, открыть файл 1CEStart.cfg, вручную прописывать путь установки клиента 1С и указать логин пользователя.<br />
<br /> Напишем скрипт, который выполнит  следущие задачи:
> 1. Определит логин_пользователя
> 2. Проверить наличие клиентов 1С в директории логин_пользователя\AppData\Local\Program\1C 
> 3. Откроет конф. файл 1CEStart.cfg для записи и пропишет путь InstalledLocation=логин_пользователя\AppData\Local\Program\1C_ + разрядность

<br />Итог - экономия времени <br />
![result](https://github.com/legion088/configuration-setting/blob/master/img/result.png)

### Примечание:
1. Для полной автоматизации необходимо собрать скрипт в фйал .exe через pyinstaller, и запустить на проблемной машине.
2. Можно было написать скрипт и через PowerShell.
3. Если есть идеи извлечения %userprofile% для параметра InstalledLocation=%userprofile%\AppData\Local\Program\1C в самом 1CEStart.cfg, с радостью прочту ваши комментария.
