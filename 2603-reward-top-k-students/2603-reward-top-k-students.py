class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], reports: List[str], student_id: List[int], k: int) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        topStudents = []

        for i, report in enumerate(reports):
            words = report.split()
            points = 0
            for word in words:
                if word in positive_set:
                    points += 3
                elif word in negative_set:
                    points -= 1
            topStudents.append((-points, student_id[i]))

        return [id for _, id in sorted(topStudents)[:k]]
