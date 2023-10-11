```shell
python -m vene fastapienv
.\fastapienv\Scripts\activate
pip install "unicorn[standard]"
```
Change python local interpreter from .\fastapienv\Scripts\python.exe

```shell
python -m uvicorn books:app --reload
```

```shell
curl http://localhost:8000/books/?category=category2
```