def alice(keyprivate,pubkeyBob,pubkeyAlice):
    return (pubkeyBob**keyprivate)%pubkeyAlice
def bob(keyprivate,pubkeyBob,pubkeyAlice):
    return (pubkeyBob**keyprivate)%pubkeyAlice
 
keyprivateAlice=53
pubkeyBob=11
pubkeyAlice=23
keyprivateBob=7

print("Bob: Открытый ключ  {} секрктный ключ {} ".format(pubkeyBob,keyprivateBob))
print("Alice: Открытый ключ  {} секрктный ключ {} ".format(pubkeyAlice,keyprivateAlice))

aliceSends=alice(keyprivateAlice,pubkeyBob,pubkeyAlice)
bobSends=bob(keyprivateBob,pubkeyBob,pubkeyAlice)
bobComputes = aliceSends**keyprivateBob
aliceComputes = bobSends**keyprivateAlice

print ("Alice отправляет ",aliceSends) 
print ("Bob вычисляет", bobComputes%pubkeyBob)
print ("Bob отправляет", bobSends)
print ("Alice вычисляет ", aliceComputes%pubkeyBob)
