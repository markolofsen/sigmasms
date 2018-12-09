<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="http://127.0.0.1:3000">GitUpload</a> erstellt.</b></p>
<p align="center"><img src="https://github.com/markolofsen/sigmasms//blob/master/.banners/banner_de.jpg?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/sigmasms/blob/master/README_cn.md">🇨🇳 Chinese</a> | <b>🇩🇪 Deutsch</b> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README.md">🇬🇧 English</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Version = 0.1.0 <br />
Bibliotheksname = sigmasms <br />
Titel = Sigma SMS API (Python 3) <br />
Schlüsselwörter = Sigma, SMS, Gate, API, Python <br />

### Heiß zu installieren

```sh
pip3 install sigmasms==0.1.0
```


### Wie benutzt man

```python
from sigmasms import SIGMA

sigma_username = 'my_username'
sigma_password = 'my_password'

res = SIGMA(username=sigma_username, password=sigma_password).send(sender='B-Media', message='Hello Mark!!!', recipients=['+34777777777','+34777777778',])
print(res)
```



---

<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="http://127.0.0.1:3000">GitUpload</a> erstellt.</b></p>