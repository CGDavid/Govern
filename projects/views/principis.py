# Principis

# Retorna la view de la finestra de principis, on es veuen tots el resources creats d'aquest tipus.
def principis(request):
	principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})

# Si el Request es GET, retorna la view de creació del resource amb el formulari buit.
# Si el Request es POST, crea el request amb les dades obtingudes al formulari
def crearPrincipi(request):
	if request.method == 'POST':
		form = PrincipiForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el principi
			nom = form.cleaned_data['principi']
			p = Principi(nom=nom)
			p.save()
			principis = Principi.objects.all()
			return render(request, 'Principis/principis.html', {'principis': principis})
	else:
		form = PrincipiForm()
	return render(request, 'Principis/crear.html', {'form': form})

# Elimina el principi corresponent a la id
def eliminaPrincipi(request, id):
	principi = Principi.objects.filter(id=id)
	principi.delete()
	principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})

# Edició del principi correponent a la id
def editaPrincipi(request, id):
	principi = Principi.objects.filter(id=id).values('nom')[0]
	form = PrincipiForm(initial={'principi': principi.get('nom'), 'principi_id':id })
	return render(request, 'Principis/editar.html', {'form': form})

# Actualitza les dades d'un principi
def updatePrincipi(request):
	form = PrincipiForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['principi']
		principi_id = form.cleaned_data['principi_id']
		principi = Principi.objects.filter(id=principi_id).update(nom=nom)
		principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})
