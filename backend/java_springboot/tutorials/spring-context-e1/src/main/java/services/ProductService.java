package services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;
import repositories.ProductRepository;

@Service
public class ProductService {
    /**
     * REQUIRED (default): create a wrapper transaction for all
     * REQUIRES_NEW:       create individual transactions for each,
                           if one commits, cannot be rolled back by any means
     * MANDATORY:          if there's a transaction, use that. If not, throw a RuntimeException
     * NEVER:              if there's NO transactions, let it happen. If there IS, throw a RuntimeException
     * SUPPORTS:           support the execution either with or without a transaction
     * NOT_SUPPORTED:      no matter whether there's a transaction or not, execute without a transaction
     * NESTED:             create a transaction within a transaction,
                           roll back nested transaction => only nested transaction
                           roll back the wrapper transaction => roll back also the nested one even if it's already commited
     */

    /**
     * DEFAULT --> read committed:
     * READ_UNCOMMITTED: all 3 problems. Highest performance
     * READ_COMMITTED: not dirty reads, 2 problems
     * REPEATABLE_READ: only phantom read
     * SERIALIZABLE: no problems with reads. Least performance
     *
     * PROBLEMS:
     * - dirty reads (READ_UNCOMMITTED):    read 10 then it becomes 20
                                            but 20 is rolled back to 10 but you still think it's 20
     * - repeatable reads (READ_COMMITTED): read 2 prices in the same transaction
     * - phantom reads (REPEATABLE_READS):  see 2 values of the same thing out of a suddent
     *
     * T1 ----10--------------20----------> 20
     *
     * T2 ------------20--C-----------R---> 10 ???
     * -------------------------------------------------------------
     * T1 ----100--------------110---------->
     *
     * T2 ------------10--C----------------->
     */

    @Autowired
    private ProductRepository productRepository;

    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void addTenProduct(){ //create
        for (int i=1; i<=10; i++){
            productRepository.addProduct("Product " + i, 20.0);
            // if (i==5) throw new RuntimeException(":(");
        }

    } // commit

    @Transactional(rollbackFor = RuntimeException.class) // (noRollbackFor = Exception.class)
    // rolls back RuntimeException but does not roll back the checked exception
    public void addOneProduct(){
        productRepository.addProduct("Vodka", 10.0);
//        throw new RuntimeException(":'<");
        try { // If exception is thrown this way, it wont be propagated by aop => wont be rolled back
            throw new RuntimeException(":(");
        } catch (RuntimeException e){
            e.printStackTrace();
        }
    }
}
