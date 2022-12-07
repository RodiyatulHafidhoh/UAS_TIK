from urllib import request
from untirta. import FormBuku
def tambah_buku(request):
    form = FormBuku()

konteks ={
    'form': form,
}
return render(request, 'tambah-buku.html', konteks)