from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
	nome = forms.CharField(max_length=50)
	email = forms.EmailField(required=False)
	mensagem = forms.Field(widget=forms.Textarea)

	def enviar(self):
		titulo = 'Message sent.'
		destino = 'tonismar@gmail.com'
		texto = """
		Nome: %(nome)s
		E-mail: %(email)s
		Mensagem:
		%(mensagem)s
		""" % self.cleaned_data

		send_mail(
			subject=titulo,
			message=texto,
			from_email=destino,
			recipient_list=[destino],
			)

def contato(request):
	form = FormContato()
	if request.method == 'POST':
		form = FormContato(request.POST)

		if form.is_valid():
			form.enviar()
			mostrar = 'Sent'
	else:
		form = FormContato()
	return render_to_response(
		'contato.html',
		locals(),
		context_instance=RequestContext(request),
	)
