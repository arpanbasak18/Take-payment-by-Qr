
import qrcode 

# Taking upi id as a input
upi_id = input ("enter your upi id :")
#upi : //pay?pa_UPI_ID&pn_name&am_ammount&cu_CURRENCY&tn_MESSAGE

phonepe_url =f'upi://pay?pa={upi_id}&pn=recipent%20Name&mc=1234'

paytm_url = f'upi://pay?pa={upi_id}&pn=recipent%20Name&mc =1234'

googlepay_url = f'upi://pay?pa={upi_id}&pn=recipent%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)

paytm_qr = qrcode.make(paytm_url)

googlepay_qr = qrcode.make(googlepay_url)

#now save the qr code in image file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')


# now display the qr code by using the pillow libary function
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()