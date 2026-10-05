class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        count = {}
        maxi = 0

        for student_id, bench_id in students:
            if bench_id in count:
                curr_studs, stud_count = count[bench_id]
                if student_id not in curr_studs:
                    curr_studs.append(student_id)
                    stud_count += 1
                count[bench_id] = (curr_studs, stud_count)
            else:
                count[bench_id] = ([student_id], 1)
            maxi = max(maxi, count[bench_id][1])
        
        return maxi