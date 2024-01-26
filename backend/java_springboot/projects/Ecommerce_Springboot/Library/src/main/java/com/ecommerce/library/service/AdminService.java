package com.ecommerce.library.Service;

import com.ecommerce.library.dto.AdminDto;
import com.ecommerce.library.model.Admin;

public interface AdminService {
    Admin findByUserName(String username);

    Admin save(AdminDto adminDto);
}

