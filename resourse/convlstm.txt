$$
\begin{aligned}
&i_t=σ(W_{xi}*\chi_t+W_{hi}*H_{t-1}+W_{ci}◦C_{t-1}+bi)\\
&f_t=σ(W_{xf}*\chi_t+W_{hf}*H_{t-1}+W_{cf}◦C_{t-1}+bf)\\
&C_t=f_t◦C_{t-1}+i_{t}◦tanh(W_{xc}*X_t+W_{hc}*H_{t-1}+b_c)\\
&o_t=σ(W_{xo}*\chi_t+W_{ho}*H_{t-1}+W_{co}◦C_{t}+bf)\\
&H_t=o_t◦tanh(C_t)\\
\end{aligned}
$$

