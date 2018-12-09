<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://sigmasms.com"><img src="https://github.com/markolofsen/sigmasms//blob/master/.banners/banner_es.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/sigmasms/blob/master/README_de.md">🇩🇪 Deutsch</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README.md">🇬🇧 English</a> | <b>🇪🇸 Spanish</b> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Versión = 0.1.3 <br />
Nombre de la biblioteca = sigmasms <br />
Título = Sigma SMS API (Python 3) <br />
Palabras clave = Sigma, SMS, Gate, API, Python <br />

### Caliente para instalar

```sh
pip3 install sigmasms==0.1.3
```


### Cómo utilizar

```python
from sigmasms import SIGMA

sigma_username = 'my_username'
sigma_password = 'my_password'

res = SIGMA(username=sigma_username, password=sigma_password).send(sender='B-Media', message='Hello Mark!!!', recipients=['+34777777777','+34777777778',])
print(res)

#Retrieving sms status
#msg_id = 'c81736cd-2919-4e6f-ac91-41bbd99fa085'
msg_id = res['id']
status = SIGMA(username=sigma_username, password=sigma_password).status(msg_id=msg_id)
print(status)
```

---

<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>