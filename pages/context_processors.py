from .models import EnquiryModal

def enquiry_modal_data(request):
    return {
        "enquiry_modal": EnquiryModal.objects.first()
    }
