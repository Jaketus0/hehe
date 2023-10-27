import qrcode

# Input text you want to convert to a QR code
text = input("Enter the text you want to convert to a QR code: ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
 
# Add the text to the QR code
qr.add_data(text)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save or display the QR code image
img.save("qr_code.png")  # Save the image as a file
img.show()  # Display the image using the default image viewer

print("QR code generated successfully.")