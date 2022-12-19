*      project3-part-b.f

************************************************************************

      real kappa
      parameter(nx=100)  
      dimension u(0:nx),unew(0:nx)
      character time*5 
      
        
      nt=4000
      jframe=nt/4  
                
                
      pi=acos(-1.0)


      kappa=54.392      
      rho=7.8*1.0e3     
      c=460.24          
*      alpha=kappa/(c*rho)
      alpha=1.0


      x0=0.0   
      xf=1.0

      t0=0.0   

 
      dx=(xf-x0)/real(nx)
      dt=0.5*dx**2/alpha


      write(*,*) 'jframe=',jframe
      write(*,*) 'dt=',dt,'  nt=',nt,'   total time=',dt*nt
      write(*,*) 'dx=',dx,'  nx=',nx,'   total length=',dx*nx


      open(10,file='project3-part-b.dat')
      write(10,*) '#   x (m)           T_calc (C)     T_analit (C)'
      
      do i=0,nx
        x=x0+i*dx
        u(i)=sin(pi*x)
        write(10,100) x,u(i),u(i) 
      end do
      close(10)


      const=alpha*dt/dx**2


      do j=1,nt    
        t=t0+j*dt

        do i=1,nx-1 
         
          x=x0+i*dx
          unew(i)=u(i)+const*(u(i+1)-2.0*u(i)+u(i-1)) 
                
          ut=1.0*exp(-pi**2*t*alpha/xf**2)*sin(pi*x/xf)   
        end do


        do i=1,nx-1
          u(i)=unew(i)
        end do


        do jj=1,5  
          if (j.eq.jframe*jj) then
          
          write(time,'(i5)') j  
          open(40,file='project3-part-b-time-'//time//'.dat')
          
          suma=0.0
          do i=0,nx
            x=x0+i*dx
            
            ut=1.0*exp(-pi**2*t*alpha/xf**2)*sin(pi*x/xf)
            
            suma=suma+(ut-u(i))**2
          end do
          amse=suma/(nx+1)
          
          end if
        end do
        
        write(40,*) '#    time= ',t,' s'
        write(40,*) '#   x (m)           T_calc (C)     T_analitc (C)'
        write(40,*) '#    MSE= ', amse
        
        do i=0,nx
          x=x0+i*dx
          
          ut=1.0*exp(-pi**2*t*alpha/xf**2)*sin(pi*x/xf)     
             
          write(40,100) x,u(i),ut
        end do
        close(40)
      end do
      
      
      

      write(*,*) 'Program Finished'
      stop
100   format(3(3x,g12.4))
      end
