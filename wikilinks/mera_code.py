def ghar(current):
	print current
	a=open("/home/amitgupta/Wiki/wiki/wikilinks/templates/"+current+".html")
	c= a.readlines()
	script = "<script type=\"text/javascript\" src=\"{% static 'js/timer.js' %}\"></script><script type=\"text/javascript\" src=\"{% static 'js/back.js' %}\"></script><script type=\"text/javascript\" src=\"{% static 'js/right.js' %}\"></script>"
	body="oncontextmenu=\"return false\">"
	

	our_line = "<a style=\"color:black;font-size:35px;font-family:wiki\" id=\"timer\">00:00</a><br>"
	zol = "{% load staticfiles %}"
	flag=False
	d=""
	index = len(c)-2
	zolindex = -3
	zolflag=False

	for i in range(len(c)):
		if "{{" in c[i] or "}}" in c[i]:
			h = c[i].split("{{")
			d += h[0]

			h = c[i].split("}}")
			d += h[-1]

			d += " "
			continue
		if "<body" in c[i]:
			d+= c[i][:len(c[i])-2]+body
		if i==zolindex:
			d += zol
		if i==index:
			d+=script
		if zolflag==False and "<head>" in c[i]:
			zolindex= i+1
			zolflag=True
		if flag==False and "ca-talk" in c[i]:
			flag=True
			d+=(our_line)
		else:
			d+=(c[i])

	a.close()
	#d+=script
	b=open("/home/amitgupta/Wiki/wiki/wikilinks/templates/"+current+".html","w")
	b.write(d)
	b.close()


