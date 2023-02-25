# phpapp

PHPApp é um aplicativo desenvolvido em Python que permite desenvolver e rodar aplicativos em PHP no desktop.

Assim que você iniciar o PHPApp irá iniciar o servidor embutido do PHP com uma porta aleatória que não está sendo usada, dessa forma é possível usar dois ou mais aplicativos ao mesmo tempo, sem que um interrompa o servidor do outro.

Para que o PHPApp funcione é necessário ter o php-cli instalado.

## Requerimento

- Sistema Operacional: GNU/Linux
- Python: 3
- GTK: 3.0
- WebKit2: 4.0
- php-cli

Testado na distro Lubuntu

## Aplicando permissão de execução

Para que o aplicativo possa rodar é necessário aplicar a permissão de execução.

```sh
chmod +x phpapp.py
```

# Usando o PHPApp

- Abra o terminal e digite chmod +x phpapp.py

- Após isso você já pode clicar duas vezes no phpapp.py e ele irá rodar.

- Os arquivos PHP devem ser armazenados na pasta www, para que funcione corretamente você deve criar um arquivo "index.php", pois esse é o arquivo principal.
