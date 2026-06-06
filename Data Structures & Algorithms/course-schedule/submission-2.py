class Course:
    def __init__(self, courseNumber):
        self.courseNumber = courseNumber
        self.dependencies = [] # will contain Courses
    
    def addDependency(self, dependency):
        self.dependencies.append(dependency)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}

        for i in range(numCourses):
            courseMap[i] = Course(i)
        
        for [courseNumber, dependency] in prerequisites:
            course = courseMap[courseNumber]
            course.addDependency(courseMap[dependency])

        for course in range(numCourses):
            start_course = courseMap[course]
            prereqTraversal = [(dep, {course}) for dep in start_course.dependencies]
            
            while len(prereqTraversal) > 0:
                prereq, path_visited = prereqTraversal.pop(0) # pop(0) makes it a true BFS queue
                if prereq.courseNumber in path_visited: 
                    return False
                
                new_path = path_visited.copy()
                new_path.add(prereq.courseNumber)
      
                # Add dependencies to the queue bundled with their respective history
                for next_dep in prereq.dependencies:
                    prereqTraversal.append((next_dep, new_path))
        
        return True