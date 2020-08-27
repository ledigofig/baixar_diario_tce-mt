#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests


# In[12]:


ultima_publi_acesso = int(input(" informe a ultima públicação que vocẽ viu? "))


# In[13]:


ultima_publi_tce = int(input(" informe a ultima públicaçãode diario que TCE-MT fez "))


# In[18]:


for indice in range(ultima_publi_acesso, (ultima_publi_tce + 1)):
    resposta = requests.get(f'https://www.tce.mt.gov.br/uploads/doe/2020/08/{indice}/diario_oficial_eletronico_{indice}.pdf')
    with open(f'Diario_TCE {indice}', 'wb') as pdf_tce:
        pdf_tce.write(resposta.content)
        
    print(f'Diario_TCE {indice}')


# In[ ]:




