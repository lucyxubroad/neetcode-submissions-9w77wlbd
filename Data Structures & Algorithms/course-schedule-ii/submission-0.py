class Course:
    def __init__(self, courseNumber):
        self.courseNumber = courseNumber
        self.dependents = [] # will contain Courses
        self.numDependencies = 0
    
    def addDependent(self, dependency):
        self.dependents.append(dependency)
        dependency.numDependencies+=1

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {}
        for i in range(numCourses):
            courseMap[i] = Course(i)
        
        for [courseNumber, dependency] in prerequisites:
            course = courseMap[dependency]
            course.addDependent(courseMap[courseNumber])

        courseOrder = []
        courseTraverse = []

        for course in range(numCourses):
            if courseMap[course].numDependencies == 0:
                courseTraverse.append(courseMap[course])

        while len(courseTraverse) > 0:
            visiting = courseTraverse.pop(0)
            courseOrder.append(visiting.courseNumber)
            for dependent in visiting.dependents:
                dependent.numDependencies-=1
                if dependent.numDependencies == 0:
                    courseTraverse.append(dependent)

        if len(courseOrder) == numCourses:
            return courseOrder
        else:
            return []
        