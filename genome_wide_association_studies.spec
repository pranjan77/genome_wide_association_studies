/*
A KBase module: genome_wide_association_studies
*/

module genome_wide_association_studies {
    /*
        Insert your typespec information here.
    */


typedef structure {
        string input_shock_id;
        string input_file_path;
    } import_gwas_data_params;



typedef structure {
        string report_ref;
        string report_name;
    } Run_import_gwas_data_result;


funcdef import_gwas_data(import_gwas_data_params)
        returns (Run_import_gwas_data_result) authentication required;


};
