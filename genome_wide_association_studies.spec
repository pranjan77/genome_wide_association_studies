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

typedef structure {
        string input_shock_id;
        string input_file_path;
    } import_snp_data_params;

typedef structure {
        string report_ref;
        string report_name;
    } Run_import_snp_data_result;

typedef structure {
        string input_shock_id;
        string input_file_path;
    } import_trait_data_params;

typedef structure {
        string report_ref;
        string report_name;
    } Run_import_trait_data_result;

typedef structure {
        string input_shock_id;
        string input_file_path;
    } import_network_data_params;

typedef structure {
        string report_ref;
        string report_name;
    } Run_import_network_data_result;



funcdef import_gwas_data(import_gwas_data_params)
        returns (Run_import_gwas_data_result) authentication required;

funcdef import_snp_data(import_snp_data_params)
        returns (Run_import_snp_data_result) authentication required;

funcdef import_trait_data(import_trait_data_params)
        returns (Run_import_trait_data_result) authentication required;

funcdef import_network_data(import_network_data_params)
        returns (Run_import_network_data_result) authentication required;



};
