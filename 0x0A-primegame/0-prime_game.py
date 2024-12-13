#!/usr/bin/python3
"""Prime Game"""


def generatePrimeNumbers(limit):
  """Generates a list of prime numbers stopping at limit"""
  primeNumbers = []
  sieveList = [True] * (limit + 1)
  for potentialPrime in range(2, limit + 1):
    if sieveList[potentialPrime]:
      primeNumbers.append(potentialPrime)
      for multiple in range(potentialPrime, limit + 1, potentialPrime):
        sieveList[multiple] = False
  return primeNumbers


def isWinner(numRounds, roundValues):
  """Determines the winner of the game"""
  if not numRounds or not roundValues:
    return None
  mariaScore = benScore = 0
  for x in range(numRounds):
    primes = generatePrimeNumbers(roundValues[x])
    if len(primes) % 2 == 0:
      benScore += 1
    else:
      mariaScore += 1
  if mariaScore > benScore:
    return "Maria"
  elif mariaScore < benScore:
    return "Ben"
  return None