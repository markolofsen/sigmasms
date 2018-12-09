<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>
<p align="center"><a href="https://sigmasms.com"><img src="https://github.com/markolofsen/sigmasms//blob/master/.banners/banner_de.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><b>🇩🇪 Deutsch</b> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README.md">🇬🇧 English</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

# Sigma SMS API (Python3)
## SMS API für Unternehmen

Version = 0.1.4 <br />
Bibliotheksname = sigmasms <br />
Titel = Sigma SMS API (Python 3) <br />
Schlüsselwörter = Sigma, SMS, Gate, API, Python <br />

### Heiß zu installieren

```sh
pip3 install sigmasms==0.1.4
```


### Wie benutzt man

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

<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>