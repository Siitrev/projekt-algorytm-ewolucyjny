from core.template.template import Population, Person
import numpy as np


class Strategy:
    def best_selection(
        self, population: Population, amount: int, maximization=False
    ) -> list[Person]:
        sample = sorted(
            population.people, reverse=maximization, key=lambda person: person.value
        )[:amount]
        return sample

    def tournament_selection(
        self,
        population: Population,
        tournaments: int,
        amount_of_contestants: int,
        maximization=False,
    ) -> list[Person]:
        sample = []
        for _ in range(tournaments):
            tournament = list(
                np.random.choice(
                    population.people, amount_of_contestants, replace=False
                )
            )
            print(tournament)
            if maximization:
                best_contestant = max(tournament, key=lambda person: person.value)
            else:
                best_contestant = min(tournament, key=lambda person: person.value)
            sample.append(best_contestant)
        return sample

    def roulette_wheel(
        self, population: Population, amount: int, maximization=False
    ) -> list[Person]:
        if maximization:
            minimum_person = min(population.people, key=lambda person: person.value)
            minimum_value = np.fabs(minimum_person.value)
            sum_of_fitness = sum(
                [person.value + minimum_value + 0.1 for person in population.people]
            )
        else:
            minimum_person = min(population.people, key=lambda person: 1 / person.value)
            minimum_value = np.fabs(1 / minimum_person.value)
            sum_of_fitness = sum(
                [1 / person.value + minimum_value + 0.1 for person in population.people]
            )
        probability = tuple(
            enumerate(
                [
                    (1 / person.value + minimum_value + 0.1) / sum_of_fitness
                    for person in population.people
                ]
            )
        )
        sample = []
        for _ in range(amount):
            wheel_result = np.random.rand()
            distribution = 0
            for ind, prob in probability:
                if wheel_result > distribution and wheel_result < distribution + prob:
                    sample.append(population.people[ind])
                    break
                distribution += prob

        return sample