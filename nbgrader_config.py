# conda install -c conda-forge nbgrader

c = get_config()
c.CourseDirectory.course_id = "sqt-skoltech"
c.Exchange.root = ".."
c.ExchangeList.inbound = False
c.ClearSolutions.code_stub = {"python": "# YOUR CODE HERE",
                              "matlab": "% YOUR CODE HERE",
}