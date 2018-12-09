<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="http://127.0.0.1:3000">GitUpload</a>.</b></p>

<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/sigmasms/blob/master/README_cn.md">🇨🇳 Chinese</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_de.md">🇩🇪 Deutsch</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README.md">🇬🇧 English</a> | <b>🇪🇸 Spanish</b> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Variable de muestra para repo: 

Versión = 0.0.9 <br />
Nombre de la biblioteca = sigmasms <br />
Título = Sigma SMS API (Python 3) <br />
Palabras clave = Sigma, SMS, Gate, API, Python <br />

### Caliente para instalar

```sh
pip3 install sigmasms==0.0.9
```


### Cómo utilizar

```python
from sigmasms import SIGMA

sigma_username = 'my_username'
sigma_password = 'my_password'

res = SIGMA(username=sigma_username, password=sigma_password).send(sender='B-Media', message='Hello Mark!!!', recipients=['+34777777777','+34777777778',])
print(res)
```



---

<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="http://127.0.0.1:3000">GitUpload</a>.</b></p>