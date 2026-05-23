class JobMarketplace: 
    def __init__(self):
        self.job_listings = []
        self.resumes = []



    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions, and add the position information to the job_listings list.
        :param job_title: The title of the position, str.
        :param company: The company of the position, str.
        :param requirements: The requirements of the position, list.
        :return: None
        """
        job_info = {'job_title': job_title, 'company': company, 'requirements': requirements}
        self.job_listings.append(job_info)
    

    def remove_job(self, job):
        """
        This function is used to remove positions, and remove the position information from the job_listings list.
        :param job: The position information to be removed, dict.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']}]
        >>> jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        >>> jobMarketplace.job_listings
        []

        """
        self.job_listings.remove(job)


    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes, and add the resume information to the resumes list.
        :param name: The name of the resume, str.
        :param skills: The skills of the resume, list.
        :param experience: The experience of the resume, str.
        :return: None
        """
        resume = {'name': name, 'skills': skills, 'experience': experience}
        self.resumes.append(resume)
    

    def withdraw_resume(self, resume):
        """
        This function is used to withdraw resumes, and remove the resume information from the resumes list.
        :param resume: The resume information to be removed, dict.
        :return: None
        """
        self.resumes.remove(resume)
    

    def search_jobs(self, criteria):
        """
        This function is used to search for positions and return the position information that meets the requirements.
        :param criteria: The requirements of the position, str.
        :return: The position information that meets the requirements, list.
        """
        matching_jobs = []
        for job in self.job_listings:
            if criteria in job['requirements']:
                matching_jobs.append(job)
        return matching_jobs
    

    def get_job_applicants(self, job):
        matching_applicants = []
        for resume in self.resumes:
            if self.matches_requirements(resume, job):
                matching_applicants.append(resume)
        return matching_applicants