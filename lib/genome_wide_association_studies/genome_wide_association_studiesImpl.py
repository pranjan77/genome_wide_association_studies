# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class genome_wide_association_studies:
    '''
    Module Name:
    genome_wide_association_studies

    Module Description:
    A KBase module: genome_wide_association_studies
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def import_gwas_data(self, ctx, import_gwas_data_params):
        """
        :param import_gwas_data_params: instance of type
           "import_gwas_data_params" (Insert your typespec information here.)
           -> structure: parameter "input_ref" of String, parameter
           "output_workspace" of String
        :returns: instance of type "Run_import_gwas_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_gwas_data
        #END import_gwas_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_gwas_data return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
