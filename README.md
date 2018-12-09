<p align="center"><b>🛠️ This repository was created using the <a href="http://127.0.0.1:3000">GitUpload</a>.</b></p>

<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/sigmasms/blob/master/README_cn.md">🇨🇳 Chinese</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_de.md">🇩🇪 Deutsch</a> | <b>🇬🇧 English</b> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/sigmasms/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Sample variable for repo: 

Version = 0.0.9 <br />
Library name = sigmasms <br />
Title = Sigma SMS API (Python 3) <br />
Keywords = Sigma, SMS, Gate, API, Python <br />

### Hot to install

```sh
pip3 install sigmasms==0.0.9
```
                    

### How to use

```python
from sigmasms import SIGMA

sigma_username = 'my_username'
sigma_password = 'my_password'

res = SIGMA(username=sigma_username, password=sigma_password).send(sender='B-Media', message='Hello Mark!!!', recipients=['+34777777777','+34777777778',])
print(res)
```
                

    

---

<p align="center"><b>🛠️ This repository was created using the <a href="http://127.0.0.1:3000">GitUpload</a>.</b></p>