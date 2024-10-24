# QR Generator

## Опис
Цей скрипт дозволяє створювати QR-коди для будь-яких URL-адрес з можливістю налаштування версії QR-коду, рівня корекції помилок, розміру квадратних елементів та товщини бордюру. Параметри можуть бути змінені через командний рядок, або використовуватись за замовченням.

## Необхідні залежності
Для коректної роботи скрипта потрібна бібліотека `qrcode` для створення QR-кодів та бібліотека `Pillow` для збереження зображень.

### Встановлення залежностей:
- Установіть Python (версія 3.x).
- Встановіть необхідні бібліотеки за допомогою pip:
```bash
pip install qrcode[pil]
```

## Структура скрипта
**Імпорт бібліотек**

- `qrcode` — для генерації QR-коду.
- `argparse` — для парсингу аргументів командного рядка.

**Функції скрипта:**

- `create_qr_code` — основна функція для створення та збереження QR-коду:

    **Параметри:**

    | Name    | Default  | Description    |
    | ------- | -------- | -------------- |
    | `url`*  |  -       | **required** </br>URL-адреса, для якої генерується QR-код. | 
    | `version` | `1`    | розмір QR-коду (кількість рядків та колонок) |
    | `error_correction` | `L`            | рівень корекції помилок (L, M, Q або H)** |
    | `box_size` | `10`  | розмір одного квадратного елемента QR-коду (в пікселях) |
    | `border`   | `4`   | товщина бордюру |
    | `output_file` | `qr_code.png` | назва вихідного файлу для збереження QR-коду |

    Пояснення параметрів:
 
   ** 
    L (7% корекції),
    M (15% корекції),
    Q (25% корекції),
    H (30% корекції).

- `main` — функція для обробки аргументів командного рядка за допомогою argparse і виклику функції create_qr_code з відповідними параметрами.

## Аргументи командного рядка:

1. Обов'язкові аргументи:
   - `url` — URL-адреса для генерації QR-коду.
2. Необов'язкові аргументи:
   - `--version`: версія QR-коду (1-40, за замовченням 1).
   - `--error_correction`: рівень корекції помилок (L, M, Q, H, за замовченням 'L').
   - `--box_size`: розмір боксу в пікселях (за замовченням 10).
   - `--border`: товщина бордюру в пікселях (за замовченням 4).
   - `--output`: шлях для збереження файлу (за замовченням qr_code.png).

Щоб переглянути довідку (help) до скрипта, можна скористатися вбудованою функцією argparse, яка автоматично генерує довідкову інформацію про всі доступні аргументи командного рядка. Для цього потрібно додати прапорець -h або --help під час запуску скрипта.

Ось приклад команди для перегляду довідки до вашого скрипта:

```bash
python qr_generator.py --help
```

Або короткий варіант:

```bash
python qr_generator.py -h
```

Це виведе наступну інформацію (приклад):
```bash
usage: qrCodeGen.py [-h] [--version VERSION] [--error_correction {L,M,Q,H}]
                    [--box_size BOX_SIZE] [--border BORDER] [--output OUTPUT]
                    url

QR Code Generator for a website.

positional arguments:
  url                   Website URL to generate the QR code for

options:
  -h, --help            show this help message and exit
  --version VERSION     QR code version (default is 1)
  --error_correction {L,M,Q,H}
                        Error correction level (default is 'L')
  --box_size BOX_SIZE   Box size (default is 10)
  --border BORDER       Border thickness (default is 4)
  --output OUTPUT       Output file name (default is 'qr_code.png')
```

## Приклади використання:

Створення QR-коду зі значеннями за замовченням:

```bash
python qrCodeGen.py https://your-website.com
```

Зміна версії QR-коду та збереження з іншим іменем файлу:

```bash
python qrCodeGen.py https://your-website.com --version 5 --output my_qr_code.png
```

Налаштування розміру боксу та рівня корекції помилок:

```bash
python qrCodeGen.py https://your-website.com --box_size 8 --error_correction H
```

