<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="http://127.0.0.1:3000">GitUpload</a>.</b></p>
<p align="center"><img src="https://github.com/markolofsen/sigmasms//blob/master/.banners/banner_ru.jpg?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/sigmasms/blob/master/README_cn.md">🇨🇳 Chinese</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_de.md">🇩🇪 Deutsch</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README.md">🇬🇧 English</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <b>🇷🇺 Russian</b></p>

---

Версия = 0.1.0 <br />
Название библиотеки = sigmasms <br />
Название = Sigma SMS API (Python 3) <br />
Ключевые слова = Sigma, SMS, Gate, API, Python <br />

### Горячая установка

```sh
pip3 install sigmasms==0.1.0
```


### Как пользоваться

```python
from sigmasms import SIGMA

sigma_username = 'my_username'
sigma_password = 'my_password'

res = SIGMA(username=sigma_username, password=sigma_password).send(sender='B-Media', message='Hello Mark!!!', recipients=['+34777777777','+34777777778',])
print(res)
```



---

<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="http://127.0.0.1:3000">GitUpload</a>.</b></p>