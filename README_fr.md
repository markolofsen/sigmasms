<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><img src="https://github.com/markolofsen/sigmasms//blob/master/.banners/banner_fr.jpg?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/sigmasms/blob/master/README_de.md">🇩🇪 Deutsch</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README.md">🇬🇧 English</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_es.md">🇪🇸 Spanish</a> | <b>🇫🇷 French</b> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Version = 0.1.1 <br />
Nom de la bibliothèque = sigmasms <br />
Titre = Sigma SMS API (Python 3) <br />
Mots-clés = Sigma, SMS, Gate, API, Python <br />

### Chaud à installer

```sh
pip3 install sigmasms==0.1.1
```


### Comment utiliser

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

<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>