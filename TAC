import React from 'react'
import { Grid } from '@mui/material'
import {Typography} from '@mui/material'
import useMediaQuery from '@mui/material/useMediaQuery';
function TermandCondition ()  {
    const mobile = useMediaQuery('(max-width:600px)');
  return (
    <>
     <Grid container md={12} xs={12} lg={12}>
     <Grid item md={12} xs={12}>
       <Typography variant='h2' sx={{textAlign:mobile?"center":'center',fontSize:mobile?'20px':'36px',marginTop:mobile?'80px':'35px',marginLeft:mobile?"0px":"0px",fontWeight:'700'}}>Terms and Conditions</Typography> 
        </Grid>
     </Grid>
     <Grid container md={12} xs={12} lg={10}  sx={{margin:'auto',marginTop:'36px'}}>
        <Grid item md={12} xs={12} lg={9.5} sx={{margin:'auto'}}>
        <ul style ={{listStyle: 'disc'}}>
        <li>
        <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
        The submitted manuscripts will be reviewed and judged by a panel of qualified judges selected by Nu Voice Press.
        </Typography>
            </li>
            <li>
            <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
         All manuscripts will be treated as confidential and will not be shared with any third party without the participant's permission.<br/>             </Typography>
                </li>
                <li>
                <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
        The judges' decision will be final, and no correspondence will be entered into.<br/> 
            </Typography>
                    </li>
                    <li>
                    <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
        Nu Voice Press reserves the right to reject any submission that does not comply with the rules and guidelines of the contest or that is deemed inappropriate or offensive.<br/> 
            </Typography>
                    </li>
                    <li>
                    <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
      By submitting their work, participants grant Nu Voice Press the right to use their name, photograph, and biographical information for promotional purposes related to the contest.<br/> 
            </Typography>
                    </li>
                    <li>
                    <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
  If the participant is selected as the winner, they will be offered a publishing agreement along with the advance with Nu Voice Press. The terms of the agreement will be negotiated on an individual basis.<br/>          </Typography>
                    </li>
                    <li>
                    <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
 Nu Voice Press is not responsible for any loss or damage to the manuscripts or other materials submitted by participants.<br/>
            </Typography> 
                    </li>
                    <li>
                    <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
 Participants acknowledge that Nu Voice Press may already be publishing or considering publishing works similar to those submitted to this contest, and waive any claims that they may have against Nu Voice Press as a result of such publication.<br/> 
        </Typography>  
                    </li>
                    <li>
                    <Typography sx={{  marginTop:mobile?'0px':"0px",marginLeft:mobile?'0px':"0px",fontSize:mobile?'14px':'18px',  lineHeight:mobile?'20px':'28px',textAlign:'initial'}}>
 Nu Voice Press reserves the right to modify the terms and conditions of the contest at any time without notice.
            </Typography>   
                    </li>
                   

                    </ul>
        
        </Grid>
     </Grid>
    </>
  )
}

export default TermandCondition
