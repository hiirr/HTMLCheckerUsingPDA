# HTML Checker Using PDA
Pada tugas besar IF2121 Logika Komputasional kali ini, kami diminta untuk membuat sebuah HTML Checker menggunakan metode Pushdown Automata (PDA). 


## What is Pushdown Automata (PDA)?
Pushdown Automata (PDA) adalah model mesin otomata yang digunakan untuk mengenali bahasa bebas konteks. PDA direpresentasikan sebagai mesin yang dilengkapi dengan penyimpanan tambahan berupa tumpukan (stack). Tumpukan adalah struktur data yang memungkinkan penyimpanan dan pengambilan data sesuai dengan prinsip Last In First Out (LIFO), di mana elemen yang terakhir dimasukkan akan menjadi yang pertama dikeluarkan.

```shell
Q  : himpunan state (set of states)
∑  : alfabet input (input symbols)
Γ  : alfabet/simbol stack (stack symbols)
q0 : state awal (start state)
Z  : simbol awal stack (start stack symbol)
F  : himpunan state penerima (final states)
δ  : fungsi transisi (transition functions/rules)
```

Simbol-simbol di atas merupakan simbol yang digunakan dalam Pushdown Automata. Selain simbo, PDA menggunakan aturan dalam metodenya. Aturan tersebut tersusun pada file pda.txt kami dengan format sebagai berikut,

```shell
[current state] [input word] [top of stack] [next state] [element to push] 
```

## How to use?
Untuk menggunakan program HTML Checker dengan PDA bisa dengan melakukan clone repository ini dengan mengetikkan,

```shell
git clone https://github.com/shulhajws/HTMLCheckerUsingPDA.git
```
Setelah melakukan clone, langsung menuju folder bernama src dan melakukan run pada file `main.py`. Setelah itu, program akan meminta untuk memasukkan sebuah file HTML.

```shell
Tuliskan nama file HTML yang akan dicek:
```
Apabila file HTML tersebut tidak ada, maka program akan meminta untuk memasukkan file lagi. Apabila file tersebut tidak memiliki kesalahan sintaks maka program akan menampilkan tampilan seperti berikut,

```shell
Accepted
```
Sedangkan, apabila file memiliki kesalahan sintaks pada file HTML akan menampilkan tampilan sebagai berikut,

```shell
Syntax Error
```
dan menampilkan letak kesalahan dari file tersebut.
 
 contoh ketika memasukkan salah satu file HTML bernama `reject5.html` pada folder test repository ini, 

![Alt text](image-1.png)

## Links

Berikut link dari diagram rancangan PDA pada program ini.

`https://drive.google.com/file/d/1gq2MWJwzamalVcAtSkjLfzD2uBFNJPBi/view?usp=sharing`