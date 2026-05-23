class JobMarketplace: 
    def __init__(self):
        self.job_listings = []
        self.resumes = []











    def search_jobs(self, criteria):
        """
        This function is used to search for positions,and return the position information that meets the requirements.
        :param criteria: The requirements of the position,str.
        :return: The position information that meets the requirements,list.
        """
        result = []
        for job in self.job_listings:
            if criteria in job['requirements']:
                result.append(job)
        return result

    def get_job_applicants(self, job):
        """
        This function is used to obtain candidate information,and return the candidate information that meets the requirements by calling the matches_requirements function.
        :param job: The position information,dict.
        :return: The candidate information that meets the requirements,list.
        """
        applicants = []
        for resume in self.resumes:
            if self.matches_requirements(resume['skills'], resume['experience'], job['requirements']):
                applicants.append(resume)
        return applicants