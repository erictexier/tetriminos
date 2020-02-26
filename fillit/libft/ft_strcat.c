/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 11:03:32 by etexier           #+#    #+#             */
/*   Updated: 2019/11/07 11:04:26 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strcat(char *dest, const char *src)
{
	char *return_val;

	return_val = dest;
	while (*dest)
	{
		dest++;
	}
	ft_strcpy(dest, src);
	return (return_val);
}
