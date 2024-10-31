# QR Generator

## Description
This script allows you to generate QR codes for any URLs with the ability to customize the version of the QR code, error correction level, square element size, and border thickness. Parameters can be modified via the command line or used with default values.

## Required Dependencies
The script requires the `qrcode` library to generate QR codes and the `Pillow` library to save the images.

### Installing Dependencies:
- Install Python (version 3.x).
- Install the necessary libraries via pip:
    ```bash
    pip install qrcode[pil]
    ```

## Script Structure
**Library Imports**

- `qrcode` — for generating QR codes.
- `argparse` — for parsing command-line arguments.

**Script Functions:**

- `create_qr_code` — the main function for creating and saving a QR code:

    **Parameters:**

    | Name    | Default  | Description    |
    | ------- | -------- | -------------- |
    | `url`*  |  -       | **required** </br>The URL for which the QR code is generated. | 
    | `version` | `1`    | QR code size (number of rows and columns) |
    | `error_correction` | `L`            | Error correction level (L, M, Q, or H)** |
    | `box_size` | `10`  | Size of one square element of the QR code (in pixels) |
    | `border`   | `4`   | Border thickness |
    | `output_file` | `qr_code.png` | The output file name for saving the QR code |

    Explanation of parameters:
    
** 
    L (7% correction),
    M (15% correction),
    Q (25% correction),
    H (30% correction).

- `main` — the function for handling command-line arguments using argparse and calling the `create_qr_code` function with the appropriate parameters.

## Command-line Arguments:

1. Required arguments:
    - `url` — The URL for generating the QR code.
2. Optional arguments:
    - `--version`: QR code version (1-40, default is 1).
    - `--error_correction`: Error correction level (L, M, Q, H, default is 'L').
    - `--box_size`: Size of the box in pixels (default is 10).
    - `--border`: Border thickness in pixels (default is 4).
    - `--output`: File path for saving the QR code (default is qr_code.png).

To view help for the script, you can use the built-in argparse function, which automatically generates help information for all available command-line arguments. To do this, add the `-h` or `--help` flag when running the script.

Here is an example command to view the help information for your script:

```bash
python qr_generator.py --help
```

Or a shorter version:

```bash
python qr_generator.py -h
```

This will display the following information (example):

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

## Usage Examples:
Generating a QR code with default values:

```bash
python qrCodeGen.py https://your-website.com
```

Changing the QR code version and saving with a different file name:

```bash
python qrCodeGen.py https://your-website.com --version 5 --output my_qr_code.png
```

Setting the box size and error correction level:

```bash
python qrCodeGen.py https://your-website.com --box_size 8 --error_correction H
```

## Author
[Alona Kuznietsova](https://github.com/acvetochka)
