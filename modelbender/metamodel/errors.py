class InvalidEnterpriseYamlError(Exception):
    pass

class NamlessEnterpriseError(Exception):
    pass

class DomainlessEnterpriseError(Exception):
    pass

class InvalidDomainYamlError(Exception):
    pass

class ResourceNotFoundInDomainError(Exception):
    pass

class CanonicalResourceWithReferentialDependancyError(Exception):
    pass
