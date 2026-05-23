class JobMarketplace: 
    def __init__(self):
        self.job_listings = []
        self.resumes = []



    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions,and add the position information to the job_listings list.
        :param job_title: The title of the position,str.
        :param company: The company of the position,str.
        :param requirements: The requirements of the position,list.
        :return: None
        """
        for job in self.job_listings:
            if job["job_title"] == job_title and job["company"] == job_title:
                job["name"] = job["name"]
                job["requirements"] = [ requirements[0], requirements[1] ]
                print(f"{job['company']} is currently looking for candidates with {job['requirements']} skills and {job['experience']} experience.")
        print(f"{job['company']} has added the position to its job listing.")

    def remove_job(self, job):
        """
        This function is used to remove positions,and remove the position information from the job_listings list.
        :param job: The position information to be removed,dict.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1','requirement2']}]
        >>> jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        >>> jobMarketplace.job_listings
        []

        """
        job.remove_from_job_listings()
        return None

    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes,and add the resume information to the resumes list.
        :param name: The name of the resume,str.
        :param skills: The skills of the resume,list.
        :param experience: The experience of the resume,str.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.submit_resume("Tom", ['skill1','skill2'], "experience")
        >>> jobMarketplace.resumes
        [{'name': 'Tom','skills': ['skill1','skill2'], 'experience': 'experience'}]

        """
        # Add the resume information to the resumes list
        job_listing = self.job_listings.append(job_listing)
        job_listing.resumes.append({
            'name': name,
           'skills': skills,
            'experience': experience
        })

    def withdraw_resume(self, resume):
        """
        This function is used to withdraw resumes,and remove the resume information from the resumes list.
        :param resume: The resume information to be removed,dict.
        :return: None
        >>> jobMarketplace = JobMarketplace()
        >>> jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1','skill2'], "experience": "experience"}]
        >>> jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        >>> jobMarketplace.resumes
        []

        """
        for item in resume:
            self.remove_job(item)
            self.remove_resume(item)
            self.remove_position(item)

    def search_jobs(self, criteria):
        """
        This function is used to search for positions,and return the position information that meets the requirements.
        :param criteria: The requirements of the position,list.
        :return: The position information that meets the requirements,list.
        """
        positions = []
        for job in self.job_listings:
            if job.requirements.count(criteria) > 0:
                positions.append(job)
        return positions

    def get_job_applicants(self, job):
        """
        This function is used to obtain candidate information,and return the candidate information that meets the requirements by calling the matches_requirements function.
        :param job: The position information,dict.
        :return: The candidate information that meets the requirements,list.
        """
        job_requirements = job.get('requirements', [])
        matches = self.matches_requirements(job_requirements)
        return matches