times = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama ', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará ', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí'
print('-='*143)
print(f'Lista de times do Brasileirão: {times}')
print('-='*143)
print(f'Os cinco primeiros colocados: {times[:5]}')
print('-='*50)
print(f'Os últimos 4 são: {times[-4:]}')
print('-='*31)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*141)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*17)
