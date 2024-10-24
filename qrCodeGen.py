import qrcode
import argparse

def create_qr_code(url, version=1, error_correction='L', box_size=10, border=4, output_file="qr_code.png"):
    # Вибір рівня корекції помилок
    error_correction_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H,
    }
    
    # Створюємо QR-код
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction_levels[error_correction],
        box_size=box_size,
        border=border,
    )

    # Додаємо URL
    qr.add_data(url)
    qr.make(fit=True)

    # Генеруємо зображення
    img = qr.make_image(fill="black", back_color="white")

    # Зберігаємо в файл
    img.save(output_file)
    print(f"QR-код збережено у файл {output_file}")

def main():
    # Парсер аргументів
    parser = argparse.ArgumentParser(description="QR Code Generator for a website.")
    parser.add_argument("url", help="Website URL to generate the QR code for")
    parser.add_argument("--version", type=int, default=1, help="QR code version (default is 1)")
    parser.add_argument("--error_correction", choices=['L', 'M', 'Q', 'H'], default='L', help="Error correction level (default is 'L')")
    parser.add_argument("--box_size", type=int, default=10, help="Box size (default is 10)")
    parser.add_argument("--border", type=int, default=4, help="Border thickness (default is 4)")
    parser.add_argument("--output", default="qr_code.png", help="Output file name (default is 'qr_code.png')")
    
    # Зчитування аргументів
    args = parser.parse_args()

    # Створюємо QR-код з введеними параметрами
    create_qr_code(args.url, args.version, args.error_correction, args.box_size, args.border, args.output)

if __name__ == "__main__":
    main()
